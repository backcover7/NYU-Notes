#include "types.h"
#include "stat.h"
#include "user.h"
#define MAX_N 512
#define STDIN "_stdin"

char buf[MAX_N];

void error(){
  printf(1, "head: error\n");
  exit();
}

void head(char *fn, int n){
  int i, b, fd, line=0;

  if(strcmp(fn, STDIN)==0){
      fd=0;
  }else{
    fd = open(fn, 0);
    if(fd < 0){
      error();
    }
  }

  while((b = read(fd, buf, sizeof(buf))) > 0 && line < n){
    for(i = 0; i < b && line < n; i++)
    {
      printf(1, "%c", buf[i]);
      if(buf[i] == '\n')
      {
      	line++;
      }
    }
  }
  if(b < 0){
    close(fd);
    error();
  }
  close(fd);
}

int main(int argc, char *argv[]){
  int i, n = 10;

  if(argc <= 1){
    head(STDIN, n);
    exit();
  }

  for(i = 1; i < argc; i++){
    strcpy(buf, argv[i]);
    if(buf[0]=='-')
    {
      if ((buf[1]<=48) || (buf[1]>=58))
      {
        error();
      }
      n = atoi(buf+1);
    }else{
      head(argv[i], n);
    }
  }
  exit();
}
