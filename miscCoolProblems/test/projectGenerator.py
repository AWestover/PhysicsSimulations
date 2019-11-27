# Alek Westover
# generates the general files that you will need for a USACO project

# libraries to interact with file system
import os
import sys

projectName = "p"
if len(sys.argv) > 1:
	projectName = sys.argv[1]
else:
	projectName = input("Please input your project name\t")

while os.path.exists(projectName) and projectName != "quit":
	projectName = input("A project with that name already exists, please input a valid name, or type 'quit'\t")

# writes the various headers


pythonHeader  = """\"\"\"
ID: alek.we1
LANG: PYTHON3
TASK: {0}
\"\"\"


fin = open ("{0}.in", "r")
fout = open ("{0}.out", "w")

print(fin.readline())

fout.write("")





#________________________________#
""".format(projectName)


cHeader = """/*
ID: alek.we1
LANG: C
TASK: {0}
*/

#include <stdio.h>

//gcc {0}.c -o {0}
// ./{0}

int main()
{{

	FILE *fin  = fopen ("{0}.in", "r");
	FILE *fout = fopen ("{0}.out", "w");

	char com[6], group[6];

	fscanf (fin, "%s %s", com, group);

	fprintf (fout, "GO\n");

	return (0);

}}





/*________________________________*/
""".format(projectName)


cppHeader = """/*
ID: alek.we1
LANG: C++
TASK: {0}
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;
// g++ {0}.cpp -o {0}
//./{0}.exe

int main()
{{
	ofstream fout ("{0}.out");
	ifstream fin  ("{0}.in");

	int a;
	fin >> a;

	fout << a << endl;

	return 0;

}}




/*________________________________*/
""".format(projectName)


javaHeader = """/*
ID: alek.we1
LANG: JAVA
TASK: {0}
*/

import java.io.*;
import java.util.*;
// make sure to change input gathering function
// javac {0}.java
// java {0}

class {0} {{
  public static void main (String [] args) throws IOException {{
    BufferedReader f = new BufferedReader(new FileReader("{0}.in"));
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("{0}.out")));
    StringTokenizer st = new StringTokenizer(f.readLine());
    int i1 = Integer.parseInt(st.nextToken());
    int i2 = Integer.parseInt(st.nextToken());
    out.println(i1 + i2);
    out.close();
  }}
}}





/*________________________________*/
""".format(projectName)




if projectName != "quit":

	print("Thank you for using the USACO file generator tool")
	print("Good luck on the {} project".format(projectName))

	os.mkdir(projectName)

	fpy   = open(projectName + "/" + projectName + ".py",   "w")
	fc    = open(projectName + "/" + projectName + ".c",    "w")
	fcpp  = open(projectName + "/" + projectName + ".cpp",  "w")
	fjava = open(projectName + "/" + projectName + ".java", "w")
	fin   = open(projectName + "/" + projectName + ".in",   "w")
	fout  = open(projectName + "/" + projectName + ".out",  "w")


	fpy.write(pythonHeader)
	fc.write(cHeader)
	fcpp.write(cppHeader)
	fjava.write(javaHeader)

	fpy.close()
	fc.close()
	fcpp.close()
	fin.close()
	fout.close()

else:
	print("Goodbye")
