after update 
as

declare @userid int , @date date 


if (select userid from inserted)<>(select userid from deleted )
raiserror ('YOU ARE NOT ALLOWED TO PERFORME THIS ACTION',10 , 1)
ELSE
begin 
    set nocount on;

    set @userid = (select userid from inserted)
    set @date = (select convert(date , checktime) from inserted)


    exec calc_atten @date , @userid 
end