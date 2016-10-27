function min(a,b:word):word;
begin
  if a>b then begin
    min:=b;
  end
  else
    min:=a;
end;
var X,Y,Z,M,ans,t:word;
begin
  ans:=1000;
  read(X);
  read(Y);
  read(Z);
  read(M);
  for t:=M to 61 do
  begin
    if(t mod 15 = 0) then 
      ans:=min(ans, X+t-M);
    if(t mod 10 = 0) then
      ans:=min(ans,Y+t-M);
    if(t mod 5 = 0) then
      ans:=min(ans,Z+t-M);
  end;
  write(ans);
end.