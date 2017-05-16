#include <iostream>
#include <string>
#include <ctype.h>

std::string bool_to_word(bool value) {
  if (value <= 0) return 0;
  return value ? "Yes" : "No";
}
int main() {
  // 输入
  std::string i = "dd";
  i.length();
  bool input = true;
  // 获取年龄
  std::string ans = bool_to_word(input);
  // 输出
  std::cout << ans;
}
