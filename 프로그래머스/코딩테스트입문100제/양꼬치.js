function solution(n, k) {
  let answer = 0;
  if (n >= 10) {
    k = k - parseInt(n / 10);
    answer = n * 12000 + k * 2000;
  } else {
    answer = n * 12000 + k * 2000;
  }

  return answer;
}

/**
 * 다른사람 
 * 
 * function solution(n, k) {
    k-=~~(n/10);
    if (k < 0) k = 0;
    return n*12000+k*2000;
}
 */
