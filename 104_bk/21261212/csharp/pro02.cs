/*
	Please write the output of the following code
    public class KwayData {
        public int id { get; set; }
        public string data { get; set; }
    }
    class Program {
        static void Main(string[] args) {
            List<KwayData> AllData = new List<KwayData>() { 
                new KwayData { id = 0, data = "data1" },
                new KwayData { id = 1, data = "data1" },
                new KwayData { id = 2, data = "data2" },
                new KwayData { id = 3, data = "data1" },
                new KwayData { id = 1, data = "data2" },
                new KwayData { id = 3, data = "data3" },
                new KwayData { id = 2, data = "data1" },
                new KwayData { id = 3, data = "data2" },
                new KwayData { id = 4, data = "data1" },
            };
            var query = from d in AllData
                        where d.id != 0
                        group d by d.id into grouped
                        select new { name = grouped.Key, Count = grouped.Count() };
            foreach (var entry in query) {
                Console.WriteLine("{0}: {1}", entry.name, entry.Count);
            }
    }

Ans:

*/