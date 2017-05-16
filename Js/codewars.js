function stringClean(s) { // O(len)
  var ans = '';
  for (var i= 0; i < s.length; ++i) {
    if (isNaN(s[i])||s[i] == ' ') ans += s[i];
  }
  return ans;
}
console.log(stringClean("12dd"));
