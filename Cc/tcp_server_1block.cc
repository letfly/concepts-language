#include <netinet/in.h> // AF_INET, SOCK_STREAM
#include <errno.h> // errno
#include <cstdio> // printf
#include <cstring> // memset
#include <unistd.h> // close

int main() {
  // 1. 创建码头
  // int socket(int domain, int type, int protocol);
  // 首先，domain需要被设置为``AF_INET``
  // 然后，type参数告诉内河这个socket是什么类型，“SOCK_STREAM”或是“SOCK_DGRM”。最后，只需要把protocol设置为0。
  // socket()函数只是简单的返回一个你以后可以使用的套接字描述符。如果发生错误，
  // socket()函数返回-1。全局变量errno将被设置为错误代码。（可以参考perror()的manpages）
  int server_s = socket(AF_INET, SOCK_STREAM, 0);
  // 捕获异常
  if (server_s == -1) {
    printf("create socket failed, errno is %d\n", errno);
    return -1;
  }
  // n: network; h: host; s: short; l: long. 主机的无符号短整形数转换成网格字节顺序
  struct sockaddr_in server_ip, client_ip;
  server_ip.sin_family = AF_INET; // 协议族
  server_ip.sin_port = htons(10003);
  server_ip.sin_addr.s_addr = htonl(
                                INADDR_ANY); // 该宏默认为0，也就是你的主机地址，方便可移植性
  memset(server_ip.sin_zero, 0, 8); // 8个字节
  int err = bind(server_s, (struct sockaddr *)(&server_ip),
                 sizeof(struct sockaddr));
  if (err == -1) {
    printf("bind error, errno is %d\n", errno);
    return -1;
  }
  // 最大连接数
  err = listen(server_s, 100);
  if (err == -1) {
    printf("listen error, errno is %d\n", errno);
    close(server_s);
    return -1;
  }
  // 2. 连接码头
  socklen_t client_len = sizeof(struct sockaddr);
  int s = accept(server_s, (struct sockaddr *)(&client_ip), &client_len);
  if (s == -1) {
    printf("accept error, errno is %d\n", errno);
    close(server_s);
    return -1;
  }
  // 3. 读取数据
  char buf[1024];
  read(s, buf, 100);
  printf("buf is %s\n", buf);
  // 4.关闭
  close(s);
  close(server_s);
  return 0;
}
