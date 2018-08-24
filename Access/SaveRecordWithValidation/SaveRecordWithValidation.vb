Option Compare Database

Private mSaved As Boolean

' Form.BeforeUpdate event occurs before changed data in a control or record is updated.
' Cancel parameter determines if the BeforeUpdate event occurs
Private Sub Form_BeforeUpdate(Cancel As Integer)
    If mSaved = False Then ' if the save button hasn't been pressed, don't save anything
        Cancel = True
        Me.Undo
        Cancel = False
    End If
    mSaved = False
End Sub

' Form.Current occurs when focus moves to a record, making it the current record, or when the form is refreshed or requeried
Private Sub Form_Current()
    mSaved = False
End Sub

' Occurs when the save button is clicked
Private Sub save_record_Click()
    
    ' do some "validation"
    If (StrComp(Me!favoriteColor.Value, "Lime", vbTextCompare) = 0) Then
        MsgBox "Impossible. No one likes Lime. Not saving."
        ' Return ' causes an error
        Exit Sub ' doesn't cause an error?
    End If
    
    If IsEmpty(Me!favoriteColor.Value) Or IsNull(Me!favoriteColor.Value) Then
        MsgBox "Favorite Color is empty!"
    End If

    mSaved = True
    ' Save the record if it has been modified
    If Me.Dirty Then
        Me.Dirty = False
    End If
    
    ' MsgBox Me!favoriteColor.Value
    ' MsgBox Me!age.Value
    ' MsgBox "Changes saved!"
End Sub
