
f = fopen('level5.in','r');

M=[];
while ~feof(f)
    M(end+1,:)=fscanf(f,'#%d @ %d,%d: %dx%d\n',[5,1]);
end

fclose(f);

A = zeros(2000,2000);
for i=1:size(M,1)
    x=M(i,2)+1;
    y=M(i,3)+1;
    w=M(i,4)-1;
    h=M(i,5)-1;
    A(x:x+w,y:y+h)=A(x:x+w,y:y+h)+1;
end
fprintf('Sum == %d\n',sum(sum(A>1)));

%% Part 2

for i=1:size(M,1)
    x=M(i,2)+1;
    y=M(i,3)+1;
    w=M(i,4)-1;
    h=M(i,5)-1;
    if sum(sum(A(x:x+w,y:y+h)))==(w+1)*(h+1)
        fprintf('Line: %d\n',i)
    end
end
