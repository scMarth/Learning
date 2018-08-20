Module Module1

    Function concatSomethingElse(ByVal inputString As String)
        ' you can also concatenate with &
        Return inputString & " something else..."
    End Function

    Function concatSomething(ByVal inputString As String)
        ' you can concatenate with +
        Return inputString + " something"
    End Function

    Sub printAString()
        Console.WriteLine("sub procedures don't return anything.")
    End Sub

    Sub Main()


        Dim myBool As Boolean = True
        Console.WriteLine(myBool)

        Dim someString As String = "Hello there"
        Console.WriteLine(someString)

        Console.WriteLine(concatSomething(someString))
        Console.WriteLine(concatSomethingElse(someString))
        printAString()

        Dim myInt As Integer = 32
        myInt = myInt * 2
        Console.WriteLine(myInt)

        Dim myInt2 As Integer

        myInt2 = 1 + 1
        Console.WriteLine(myInt2)

        Console.WriteLine()

        For i = 1 To 10
            Console.WriteLine(i)
        Next i

        Console.WriteLine()

        Dim count As Integer = 10

        'single line comment

        While count >= 0
            Console.WriteLine(count)
            count = count - 1
        End While

        If count = 0 Then
            Console.WriteLine("count = 0")
        ElseIf count < 0 Then
            Console.WriteLine("count < 0")
        ElseIf count > 0 Then
            Console.WriteLine("count > 0")
        ElseIf count <> 0 Then
            Console.WriteLine("count != 0")
        ElseIf count <= 0 Then
            Console.WriteLine("count <= 0")
        ElseIf count >= 0 Then
            Console.WriteLine("count >= 0")
        End If

        Dim strClasses(5) As String
        strClasses(0) = "String 1"
        strClasses(1) = "String 2"
        strClasses(2) = "String 3"
        strClasses(3) = "String 4"
        strClasses(4) = "String 5"
        strClasses(5) = "String 6"

        For num As Integer = 0 To strClasses.Length - 1
            Console.WriteLine(strClasses(num))
        Next

        ' commas

        Dim a, b, c, d As String, x, y, z As Boolean

        a = "string a"
        b = "string b"
        c = "string c"
        d = "string d"

        x = True
        y = False
        z = True

        Console.WriteLine("")

        Console.WriteLine(a)
        Console.WriteLine(b)
        Console.WriteLine(c)
        Console.WriteLine(d)

        Console.WriteLine(x)
        Console.WriteLine(y)
        Console.WriteLine(z)

        Console.ReadKey()
    End Sub

End Module
