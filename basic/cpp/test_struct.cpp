static void a(void);
static void b(void);

typedef struct 
{
    void (*const a)(void);
    void (*const b)(void);
}test_t;

test_t test =
{
    .a = a,
    .b = b,
};

static void a(void)
{
    // do something
}

static void b(void)
{
    // do something
}

void main(void)
{
    test.a();

    while (1)
    {
        /* code */
    }
    
}