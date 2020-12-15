## Integration Defect Report
| Program | Output Error | Source Code Error | Changes Made |
|---------|--------------|-------------------|--------------|
| Weekly Script | Running it broke backend pytests | Overrote accounts.csv and tickets.csv in src, which backend tests were based on | Copied original csv files to test_backend folder and made pytest read those files instead |
| Weekly Script | Account/ticket history files not named properly | File indices started with 0 | Added 1 to file indices |
| Daily Script | Frontend crashed on exit | Script input list didn't append 'exit' properly | 'exit' appended to each input array in list |
| Daily Script | Invalid program arguments | Backend function still used sys.stdin like frontend | Removed input code since backend has no input |
| Daily Script | Invalid input of 15.00 for argument int | Input string didn't account for reversed order of arguments for buy/sell/update sessions | Changed order of arguments for different inputs |