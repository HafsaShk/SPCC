#include<stdio.h>
#include<conio.h>
int isempty(int k);
int pr1(char op[],int k);
int pr(char a[],int i);
int ins()
{
    int k=-1;
    return k;
}
int isempty(int k)
{
    if(k==-1)
        return (-1);
    else
        return (k);
}
int pr(char a[],int i)
{
    int l=0;
    if((a[i]=='+')||(a[i]=='-'))
        l=1;
    else if((a[i]=='*')||(a[i]=='/'))
        l=2;
    return (l);
}
int pr1(char op[],int k)
{
    int l=0;
    if((op[k]=='+')||(op[k]=='-'))
        l=1;
    else if((op[k]=='*')||(op[k]=='/'))
        l=2;
    return (l);
}

void main()
{
    char a[40],alp[30],op[20];
    int i,n,j=0,c=0,s[20],a1;
    printf("Enter No. of Characters in Expression\n");
    scanf("%d",&n);
    printf("Enter Expression\n");
    for(i=0;i<n+1;i++)
        scanf("%c",&a[i]);
    int k=ins();
    for(i=0;i<n+1;i++)
    {
        switch(a[i])
        {
            case 'a':
            case 'b':
            case 'c':
            case 'd':
            case 'e':
                alp[j]=a[i];
                j++;
                break;

            case '+':
            case '/':
            case '*':
            case '-':
                int p1,n,p2,d=0;
                int e=isempty(k);
                if(e==-1)
                    d=1;
                else
                {
                    p1=pr(a,i);
                    p2= pr1(op,k);
                    if(p2>=p1)
                    {
                        char a1=op[k];
                        k--;
                        alp[j]=a1;
                        j++;
                    }
                    d=1;
                }
                if(d==1)
                {
                    k++;
                    op[k]=a[i];
                }
                break;
            
            case '(':
                k++;
                op[k]=a[i];
                break;

            case ')':
                int f=0;
                while(op[k]!='(')
                {
                    char c1=op[k];
                    if(c1=='(')
                        f=1;
                    else
                    {
                        alp[j]=c1;
                        j++;
                        k--;
                    }
                }
                break;
        }
    }

    int e=isempty(k);
    int f=0;
    while(k>=0)
    {
        char c1=op[k];
        k--;
        if(c1=='(')
            f=1;
        else
        {
            alp[j]=c1;
        j++;
        }
    }
    for(i=0;i<j;i++)
        printf("%c",alp[i]);
    int w=0,o=-1;
    printf("\n");
    for(i=0;i<j;i++)
    {
        switch(alp[i])
        {
            case 'a':
            case 'b':
            case 'c':
            case 'd':
            case 'e':
                w++;
                o++;
                s[o]=w;
                printf("\nMOV R%d, %c",w,alp[i]);
                break;
            case '+':
                printf("\nADD R%d, R%d",s[o-1],s[o]);
                a1= s[o];
                o--;
                s[o]=a1;
                break;
            case '-':
                printf("\nSUB R%d, R%d",s[o-1],s[o]);
                a1= s[o];
                o--;
                s[o]=a1;
                break;
            case '*':
                printf("\nMUL R%d, R%d",s[o-1],s[o]);
                a1= s[o];
                o--;
                s[o]=a1;
                break;
            case '/':
                printf("\nDIV R%d, R%d",s[o-1],s[o]);
                a1= s[o];
                o--;
                s[o]=a1;
                break;
        }
    }
}