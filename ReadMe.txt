To use FilePBE, first make sure Java 8 is installed in your machine, and then remember
to put the "input.csv, output.csv, ioMap.txt" for a task in the same directory, say, foo/bar.
Finally, to synthesize the program and verify the correctness, use the command:

    java -jar FilePBE.jar foo/bar

Test cases used in our evaluation are included in the "testcases" folder.
You can try running one with the following command:

    Windows:         java -jar FilePBE.jar testcases\benchmarks\hades-f9
    Mac/Linux/Unix:  java -jar FilePBE.jar testcases/benchmarks/hades-f9

Also, You can try new tasks by modifying the configuration files.

=== csv files ===

Fields in the csv files denotes, from left to right,
     * 0.  file name
     * 1.  extension
     * 2.  path
     * 3.  size (in Bytes)
     * 4.  modification time
     * 5.  hidden or not
     * 6.  executable or not
     * 7.  readable
     * 8.  writable
     * 9.  deleted
     * 10. example
     * 11. a unique id

Please note that using Microsoft Excel may break the formats, we strongly recommend using text editors

=== ioMap.txt ===

You can specify the mapping of the example files from input.csv to output.csv in the following ways (ix and oy are IDs in input.csv and output.csv):
     rename ix oy    // rename
     chext ix oy     // change extension
     move ix oy      // move
     chmod+x ix oy   // make executable
     chmod-x ix oy   // make non-executable
     chmod+r ix oy   // make readable
     chmod-r ix oy   // make non-readable
     chmod+w ix oy   // make writable
     chmod-w ix oy   // make non-writable
     chmod+v ix oy   // make visible
     chmod-v ix oy   // make invisible
     delete ix oy    // delete
     unzip ix oy     // unzip
     copy ix oy      // copy
     keep ix oy      // keep not changed
