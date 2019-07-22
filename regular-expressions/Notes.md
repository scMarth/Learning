153253017000,1010,1001,MELVILLE ST,,1010 MELVILLE ST,SALINAS,CA,93906,NUNEZ,ELIAS S JR & NUNEZ JANETTE Y,1010 MELVILLE ST,,SALINAS,CA,93906,"NUNEZ, ELIAS S JR & NUNEZ JANE",,,,0.000000000000000,0.000000000000000,0,0,0,0,0.000000000000000,540600.000000000000000,387600.000000000000000,005026,Alisal,,R-L-5.5,,,,,,,153000.000000000000000,ACTIVE,0,,0,,,CRW:702151243104306,,,,PARCEL,,,,,,,,,,,,,36.710514000000003,-121.610232000000000,,,32410
153253018000,1006,1001,MELVILLE ST,,1006 MELVILLE ST,SALINAS,CA,93906,GUERRERO,ERIK ,1006 MELVILLE ST,,SALINAS,CA,93906,"GUERRERO, ERIK",,,,0.000000000000000,0.000000000000000,0,0,0,0,0.000000000000000,325649.000000000000000,242857.000000000000000,005026,Alisal,,R-L-5.5,,,,,,,82792.000000000000000,ACTIVE,0,,0,,TK:010110758000004,CRW:702151243104307,,,,PARCEL,,,,,".

",,,,,,,,36.710627000000002,-121.610162000000000,,,32411
153253019000,1002,1001,MELVILLE ST,,1002 MELVILLE ST,SALINAS,CA,93906,NUNEZ,ANGELA ,1002 MELVILLE ST,,SALINAS,CA,75067,"NUNEZ, ANGELA",,,,0.000000000000000,0.000000000000000,0,0,0,0,0.000000000000000,293636.000000000000000,210844.000000000000000,005026,Alisal,,R-L-5.5,,,,,,,82792.000000000000000,ACTIVE,0,,0,,CSS:808040945000024,CRW:702151243104308,,,,PARCEL,,,,,,,,,,,,,36.710740000000001,-121.610091000000000,,,32412


Let’s say the above are 3 entries in a CSV file…. When I exported this CSV file, some entries have newlines so using python to read the CSV line by line failed. It is because there are newlines (+- carriage returns) in some values.

Luckily though, when the program exports it and something weird happens (in this case, when a value contains a line feed / newline / carriage return / comma ) the program exported the value as ,” “, Basically, it put it in quotations.

So to match instances of carriage returns / newlines in the csv, use the regular expression:

`"[^,"$]+$[^,"$]+"`

`"[^,"\n]+\n[^,"\n]+"` If you had replaced the dollar signs with \n, it would fail if the newlines contain carriage returns or line feeds

BUT when you paste something in Sublime, depending on your settings, it may or may not print the CR LF as just a LF

```
\t tab character (ASCII 0x09)
\r carriage return (0x0D)
\n line feed (0x0A)
\a bell (0x07)
\e escape (0x1B)
\f form feed (0x0C)
```

Remember that Windows text files use \r\n to terminate lines, while UNIX text files use \n

In some flavors, \v matches the vertical tab (ASCII 0x0B). In other flavors, \v is a shorthand that matches any vertical whitespace character. 

https://stackoverflow.com/questions/26124314/sublime-text-regex-not-detecting-multiline-tags

`\[sometag\](.*)\[/sometag\]`
[sometag] here is more text
it spans more than one line [/sometag]
In sublime, use (?s) to make dot to match newline characters

`(?s)\[sometag\](.*?)\[\/sometag\]`

### Positive and Negative Lookahead

`q(?=u)` matches a q that is followed by a u, without making u part of the match

`q(?!u)` matches a q that is not followed by a u, without making u part of the match

Negating string literals https://stackoverflow.com/questions/1240275/how-to-negate-specific-word-in-regex

Using negative lookahead

`^[\s]+(?!BEDROOMS).*:`

Will skip the line with bedrooms

```
    NO_STORIES: "0"
    BEDROOMS: "0"
    BATHROOMS: "0"
```


`q(?!u)` will match:

**q**ass

**q**bbb

**q**asdfasdf

**q**kffr

`q(?=u)` will match:

**q**uick

**q**udd

**q**uids


### Conditionals

https://www.regular-expressions.info/conditional.html
You can do a logical or for string literals like this:

`^[\s]+(?!SITE_APN|SITE_NUMBER|SITE_UNIT_NO).*: "`

### Matching More Than One Word

Parenthesis can be used for OR'ing string literals. 

In Javascript, You can use (x1|x2|) to match nothing after matching x1 and x2. This is a greedy type of match.

/(bike(path|way|\s*-*\s*plan|\s*-*\s*route|)|bicycle)/ig

`bike` `bikepath` `bikeway` `bicycle` `bike route` `bike plan` transportation and infrastructure

### Javascript Regex Tester

https://www.regextester.com/97356
