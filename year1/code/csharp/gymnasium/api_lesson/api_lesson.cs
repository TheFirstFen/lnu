// api_lesson.cs
//
// Author: Samuel Berg
// Date: 10-Aug-2019

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using RestSharp;


namespace API_lesson
{
    class Program
    {
        static void Main(string[] args)
        {


            var client = new RestClient("https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.158/lat/58.5812/data.json");
            var request = new RestRequest("/", Method.GET);
            IRestResponse response = client.Execute(request);
            String content = response.Content;
            RootObject rootobject = JsonConvert.DeserializeObject<RootObject>(content);
        }

        public class Geometry
        {
            public string type { get; set; }
            public List<List<double>> coordinates { get; set; }
        }

        public class Parameter
        {
            public string name { get; set; }
            public string levelType { get; set; }
            public int level { get; set; }
            public string unit { get; set; }
            public List<double> values { get; set; }
        }

        public class TimeSery
        {
            public DateTime validTime { get; set; }
            public List<Parameter> parameters { get; set; }
        }

        public class RootObject
        {
            public DateTime approvedTime { get; set; }
            public DateTime referenceTime { get; set; }
            public Geometry geometry { get; set; }
            public List<TimeSery> timeSeries { get; set; }
        }
    }
}
