#include <cstdio>
#include <cstring>
#include <netinet/in.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/epoll.h>

int main() {
  // 1. 创建码头
  // int socket（int domain , int type , int protocol）;
  // 首先，domain 需要被设置为 “AF_INET”，就像上面的struct sockaddr_in。
  // 然后，type参数告诉内核这个socket 是什么类型，“SOCK_STREAM”或是“SOCK_DGRAM”。最后，只需要把protocol 设置为0 。
  // socket()函数只是简单的返回一个你以后可以使用的套接字描述符。如果发生错误，
  // socket()函数返回 –1 。全局变量errno 将被设置为错误代码。（可以参考perror() 的manpages）
  int server_s = socket(AF_INET, SOCK_STREAM, 0);
  // 捕获异常
  if (server_s == -1) {
    printf("create socket failed, errno is %d\n", errno);
    return -1;
  }
  // n: network; h: host; s: short; l: long. 主机的无符号短整形数转换成网络字节顺序
  struct sockaddr_in server_ip, clien_ip;
  server_ip.sin_family = AF_INET; // 协议族
  server_ip.sin_port = htons(10003);
  server_ip.sin_addr.s_addr = htonl(INADDR_ANY); // 该宏默认为0，也就是你的主机地址，方便可移植性
  memset(server_ip.sin_zero, 0, 8); // 8个字节
  if (bind(server_s, (struct sockaddr *)(&server_ip), sizeof(struct sockaddr)) == -1) {
    printf("bind error, errno is %d\n", errno);
    return -1;
  }
  // 最大连接数
  if (listen(server_s, 100) == -1) {
    printf("listen error, errno is %d\n", errno);
    close(server_s);
    return -1;
  }

  // fcntl()函数，处理多路复用I/O
  int flags, client_s;
  if ((flags = fcntl(server_s, F_GETFL, 0)) < 0) perror("fcntl F_GETFL");
  flags |= O_ASYNC; // O_NONBLOCK为非阻塞I/O，O_ASYNC为信号驱动I/O
  if (fcntl(server_s, F_SETFL, flags) < 0) perror("fcntl F_SETFL");

  int epollfd = epoll_create(500);
  if (epollfd < 0) {
    perror("epoll_create err:");
    return -1;
  }
  struct epoll_event ev, events[500];
  ev.data.fd = server_s;
  ev.events = EPOLLIN;
  if (epoll_ctl(epollfd, EPOLL_CTL_ADD, server_s, &ev) == -1) {
    perror("epoll_ctl err:");
    return -1;
  }
  while (1) {
    int fds = epoll_wait(epollfd, events, 500, -1);
    if (fds < 0) {
      perror("epoll_wait err:");
      return -1;
    }

    // 轮询
    for (int i = 0; i < fds; ++i) {
      int current_s = events[i].data.fd;
      if (current_s == server_s) {
        // 2.连接码头
        socklen_t clien_len = sizeof(struct sockaddr);
        client_s = accept(server_s, (struct sockaddr *)(&clien_ip), &clien_len);
        if (client_s == -1) {
          printf("accept error, errno is %d\n", errno);
          close(server_s);
          continue;
        }

        ev.data.fd = server_s;
        ev.events = EPOLLIN | EPOLLET;
        epoll_ctl(epollfd, EPOLL_CTL_ADD, server_s, &ev);
      } else {
        // 3.读取数据
        char recv_buf[1024];
        int bytes;
        if ((bytes = recv(client_s, recv_buf, 1024, 0)) < 0) {
          perror("recv");
          close(client_s);
          epoll_ctl(epollfd, EPOLL_CTL_DEL, current_s, &ev);
          close(current_s);
          continue;
        }
        printf("recv_buf is %s\n", recv_buf);
        send(current_s, recv_buf, bytes, 0);
      }
    }

  }

  // 4.关闭
  close(client_s);
  close(server_s);
  return 0;
}
