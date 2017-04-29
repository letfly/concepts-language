#include <cstdio>
#include <cstring>
#include <netinet/in.h>
#include <unistd.h>

int main() {
  // 1.创建码头
  int s = socket(AF_INET, SOCK_STREAM, 0);
  struct sockaddr_in server_ip;
  server_ip.sin_family = AF_INET;
  server_ip.sin_port = htons(10003);
  server_ip.sin_addr.s_addr = htonl(INADDR_ANY);
  if (connect(s, (struct sockaddr*)&server_ip, sizeof(server_ip)) < 0) {
    perror("connect error");
    return 0;
  }

  // 2.发送数据
  while (1) {
    char buf[1024], read_buf[1024];
    fgets(buf, 1024, stdin);
    send(s, buf, strlen(buf), 0);

    int bytes = recv(s, read_buf, 1024, 0);
    printf("Read bytes %d\n", bytes);
    printf("read_buf: %s\n", read_buf);
  }

  // 3.关闭
  close(s);
  return 0;
}
