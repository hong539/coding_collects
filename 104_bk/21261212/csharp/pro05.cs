/*
	Please consider the following code.
using System;
public class Singleton
{
   private static Singleton instance;
   private Singleton() {}
   public static Singleton Instance
   {
      get 
      {
         if (instance == null)
         {
            instance = new Singleton();
         }
         return instance;
      }
   }
}
	
(1) What is the problem with the code above. Please explain it briefly.
(2) Please rewrite it to solve the problem.

Ans:

*/