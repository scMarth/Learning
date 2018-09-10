using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Request library
using System.Net;
using System.IO;

namespace ods_cos
{
    class Program
    {
        static void Main(string[] args)
        {

            // Get Request
            Console.WriteLine("GET\n");

            string getUrl = @"https://cityofsalinas.opendatasoft.com/api/records/1.0/search/?dataset=anonymized-crime-data";

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(getUrl);
            request.AutomaticDecompression = DecompressionMethods.GZip | DecompressionMethods.Deflate;

            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            using (Stream stream = response.GetResponseStream())
            using (StreamReader reader = new StreamReader(stream))
            {
                Console.WriteLine(reader.ReadToEnd());
            }


            // Post Request
            Console.WriteLine("\nPOST\n");

            string postUrl = @"https://cityofsalinas.opendatasoft.com/api/records/1.0/search/";

            string data = "dataset=anonymized-crime-data";
            byte[] dataBytes = Encoding.UTF8.GetBytes(data);

            request = (HttpWebRequest)WebRequest.Create(postUrl);
            request.AutomaticDecompression = DecompressionMethods.GZip | DecompressionMethods.Deflate;
            request.ContentType = "application/x-www-form-urlencoded";
            request.ContentLength = dataBytes.Length;
            request.Method = "POST";

            using (Stream requestBody = request.GetRequestStream())
            {
                requestBody.Write(dataBytes, 0, dataBytes.Length);
            }

            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            using (Stream stream = response.GetResponseStream())
            using (StreamReader reader = new StreamReader(stream))
            {
                Console.WriteLine(reader.ReadToEnd());
            }


        Console.ReadKey();
        }
    }
}
