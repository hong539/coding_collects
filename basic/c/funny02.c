#define FUN(A,B) ((A)>=(B) ? (A) : (B))

int main()
{
    int a = 12;
    int* b = &a;
    int c = 10;
    
    int least = FUN(*b++, c);
    
    printf("%d\n", least);
}