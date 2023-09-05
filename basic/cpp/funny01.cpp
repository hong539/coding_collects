int main (void)
{
    int score;
    printf("輸入總成績");
    scanf("%d,&score");
    if (score<=85)
    {
        printf("繼續努力\n");
    }
    else if(score<=90)
    {
        printf("好棒\n");
    }
    else
    {
        printf("優秀\n");
    }
    return 0;
}