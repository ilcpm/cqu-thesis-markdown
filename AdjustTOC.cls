VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisDocument"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub 目录页锟斤拷()
'
' 作用：把选中区域中的页码域代码`PAGEREF`中的页码数字设置字号
' 使用: 选中整个目录而后应用该宏即可把目录中页码的数字调整为相同大小
'
    Dim r As Range
    Set r = Selection.Range
    
    Dim f As Field
    For Each f In r.Fields
        If Left(Trim(f.Code.Text), Len("PAGEREF")) = "PAGEREF" And Right(Trim(f.Code.Text), 2) = "\h" Then
            'MsgBox "Code = " & f.code & vbCr & "Result = " & f.Result & vbCr
            
            f.Code.Text = Replace(f.Code.Text, "\h", "\h \* MERGEFORMAT")
            'f.Update
            
            'MsgBox "Code = " & f.code & vbCr & "Result = " & f.Result & vbCr
            
            With f.Result.Font
                .Bold = False
                .Italic = False
                .Size = 10.5
            End With
            
        End If
    
    Next f
    'r.Fields.Update

End Sub
