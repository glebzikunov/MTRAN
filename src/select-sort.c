int main(){
  int N = 5;
  int arr[N];
  
  for(int k = 0; k < N; k++){
    arr[k] = 10 - (k + N);
    printf("%d ", arr[k]);
  }
  
  printf("\n");

  for (int i = 0; i < (N - 1); i++){
    int min_index = i;
    for (int j = (i + 1); j < N; j++){
      if (arr[j] < arr[min_index]){
        min_index = j;
      }
    }
    if (min_index != i){
      int temp = arr[i];
      arr[i] = arr[min_index];
      arr[min_index] = temp;
    }
  }

  printf("\n");

  for(int k = 0; k < N; k++){
    printf("%d ", arr[k]);
  }

  return 0;
}