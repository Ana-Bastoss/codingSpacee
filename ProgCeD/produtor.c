#include <stdio.h>

int main(void){
    for(int i = 1; i <= 5; i++){
        printf("mensagem %d\n", i);
        fflush(stdout);
    }
}