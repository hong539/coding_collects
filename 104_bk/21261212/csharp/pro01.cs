/*
	Please fill in the blank.

a:              
b:              
c:              
d:              

public     a     class Dimensions
{
    public const double pi = Math.PI;
    protected double x, y;

    public Dimensions(double x, double y)
    {
        this.x = x;
        this.y = y;
    }

    public     b     double Area()
    {
        return x * y;
    }
}

public class Sphere : Dimensions
{
    public Sphere(double r)
        :     c    (r, 0)
    {
    }

    public     d    double Area()
    {
        return 4 * pi * x * x;
    }
}

*/

public     a     class Dimensions
{
    public const double pi = Math.PI;
    protected double x, y;

    public Dimensions(double x, double y)
    {
        this.x = x;
        this.y = y;
    }

    public double double Area()
    {
        return x * y;
    }
}

public class Sphere : Dimensions
{
    public Sphere(double r)
        :     c    (r, 0)
    {
    }

    public new double Area()
    {
        return 4 * pi * x * x;
    }
}