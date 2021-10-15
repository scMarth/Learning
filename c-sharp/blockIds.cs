using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace BlockTrialCodes
{
    class Program
    {
        static void Main(string[] args)
        {
            String blockCode = "B1";
            // String trialID = "TEST-20-001-B1";
            String trialID = "TEST-20-001-B1_1";


            String[] trialIDs = new String[] {
                "TEST-20-001-B1_1",
                "TEST-20-001-B1_2",
                "TEST-20-001-B1_3",
                "TEST-20-001-B2",
                "TEST-20-001-B3",
                "TEST-20-002-B3",
                "TEST-20-001-2B3",
                "TEST-20-001-222B3",
                "TEST-222-001-B3",
                "TESTS-20-001-B3",
                "TEST-21-001-B3",
                "TEST-21-001-B3-4999",
                "TEST-21-001-B3-A344999",
                "TEST-21-001-B3-A344999-Hello",
                "TEST-21-001-B3-A344999-Hello-A1_1",
                "TEST-21-001-B3-A344999-Hello-B2"
            };

            Regex rx = new Regex(blockCode + @"_[0-9]");

            if (trialID.EndsWith("-" + blockCode) || rx.Matches(trialID).Count > 0)
            {
                Console.WriteLine("trialID: " + trialID);
                int lastInd = trialID.LastIndexOf("-" + blockCode);

                String trueTrialID = trialID.Substring(0, lastInd);

                Console.WriteLine(lastInd);
                Console.WriteLine(trueTrialID);

                Console.WriteLine("Here are the matches:");

                Regex trialIdPattern = new Regex(trueTrialID + @"-[A-Z][0-9]+[_]*[0-9]*");
                foreach (String listedID in trialIDs)
                {
                    if (trialIdPattern.Matches(listedID).Count > 0)
                    {
                        Console.WriteLine(listedID);
                    }
                    else
                    {
                        Console.WriteLine("NOT MATCH: " + listedID);
                    }
                }

            }
            else
            {
                Console.WriteLine("Error: TrialID does not contain the block code.");
            }

            Console.ReadKey();
        }
    }
}
