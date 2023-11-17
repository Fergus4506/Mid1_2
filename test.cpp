#include <stdio.h>
#include <string.h>
#define MAX_QUEUE_SIZE 10
int global_clock=0;
typedef struct Customer 
{
    char id[20]; // 客戶 id
    int arr_time; // 客戶到達銀行時間
    int ser_time; // 客戶完成業務要花多少時間
    int wait_time; // 客戶等待多久
}Customer;
typedef struct TellerQueue
{
    int status; // status, 0: close, 1:只剩下一位客戶，即將close, 2: open
    int front; // front pointer，指向第一個element 的index
    int rear; // rear pointer，指向最後一個element 的下一個index
    int count; // queue 中在排隊的人數
    int current_served_time; // 目前在處理業務的客人已經花的時間
    Customer queue[MAX_QUEUE_SIZE]; // 以 array 型式模擬Circular Queue。
}TellerQueue;
/*int ReadOneRecord(int index,struct Customer customer,struct TellerQueue *Queue)
{
    Queue[index].front=customer.arr_time;
    Queue[index].rear=customer.ser_time;
    Queue[index].count=Queue[index].rear-Queue[index].front;
}*/
void OpenQueue(struct TellerQueue *teller_queue,int gate) //開啟窗口
{
    if(teller_queue[gate].status==0)
    {
        teller_queue[gate].status=2;
    }
}
int UpdateQueueStatus(struct TellerQueue *teller_queue,int new_arr_time,char *id,int new_ser_time,int currentQueueSize) //更新每個時間的status
{
    /*for(int i=0;i<currentQueueSize;i++)
    if (new_arr_time==global_clock&&teller_queue[i].status==2)
    {
        teller_queue[i].queue[i].id=id;
        teller_queue[i].front=global_clock;
        teller_queue[i].rear=global_clock+new_ser_time;
        teller_queue[i].status=1;
        teller_queue[i].count++;
        return 0;
    }
    for(int i=0;i<currentQueueSize;i++)
    {
        int min=100,int temp=0;
        if(new_arr_time==global_clock&&teller_queue[i].status==1)
        {
            if(teller_queue[i].count<min)
            {
                min=teller_queue[i].count;
                temp=i;
            }
        }
        teller_queue[temp].count++;
        teller_queue[temp].front
    }
    else*/
        for(int i=0;i<currentQueueSize;i++)//currentQueueSize是現在開啟窗口的數量
        if(global_clock==teller_queue[i].queue[0].ser_time+teller_queue[i].queue[0].wait_time&&teller_queue[i].status==1)//若窗口有人排隊且有人要走了
        {
            printf("%s,%d,%d",teller_queue[i].queue[0].id,teller_queue[i].queue[0].arr_time,global_clock);
            if(teller_queue[i].count>=2)
            {
                teller_queue[i].count--;
                for(int j=0;j<=teller_queue[i].count;j++)
                {
                    //endtime=arr_time+ser_time;
                    strncpy(teller_queue[i].queue[j].id,teller_queue[i].queue[j+1].id,20);
                    teller_queue[i].queue[j].arr_time=teller_queue[i].queue[j+1].arr_time;
                    teller_queue[i].queue[j].ser_time=teller_queue[i].queue[j+1].ser_time;
                    teller_queue[i].queue[j].wait_time=global_clock-teller_queue[i].queue[j+1].arr_time;
                }
            }
            else if(teller_queue[i].count==1)
            {
                teller_queue[i].count--;
                teller_queue[i].status=2;
                strncpy(teller_queue[i].queue[0].id," ",5);
                teller_queue[i].queue[0].arr_time=0;
                teller_queue[i].queue[0].ser_time=0;
                teller_queue[i].queue[0].wait_time=0;
            }
        }
        if (new_arr_time!=global_clock)
        {
            return 0;
        }
        else
            return 1;
}
// P.S. 一開始，front = 0, rear = 0
//有 10 個服務窗口，所以要有 10 個Queue 來紀錄每個窗口目前的排隊狀態，
void InsertNewCustomer( int shortest,struct TellerQueue *teller_queue,int new_arr_time,char *id,int new_ser_time)//新顧客
{
        strncpy(teller_queue[shortest].queue[teller_queue[shortest].count].id,id,20);
        teller_queue[shortest].queue[teller_queue[shortest].count].arr_time=new_arr_time;
        teller_queue[shortest].queue[teller_queue[shortest].count].ser_time=new_ser_time;
}
int GetTheShortestQueueId (int currentQueueSize,struct TellerQueue *Shortest)//找出排最少的那列
{
    int mini=10;
    int address=0;
    for(int i=0;i<currentQueueSize;i++)
    {
        if(Shortest[i].count<mini)
        {
            mini=Shortest[i].count;
            address=i;
            printf("%d\n",global_clock);
        }
    }
    return address;
}
void FromTheSecondElementInCloseQueue(struct TellerQueue *teller_queue,int gate,int currentQueueSize)
{
    for(int i=1;i<teller_queue[gate].count;i++)
    {
        InsertNewCustomer(GetTheShortestQueueId (currentQueueSize,teller_queue),teller_queue,teller_queue[gate].queue[i].arr_time,teller_queue[gate].queue[i].id,teller_queue[gate].queue[i].ser_time);
    }
}
void CloseQueue(struct TellerQueue *teller_queue,int gate,int currentQueueSize)
{
    if(teller_queue[gate].status==2)
    {
        teller_queue[gate].status=0;
    }
    else if(teller_queue[gate].status==1)
    {
        teller_queue[gate].status=0;
        FromTheSecondElementInCloseQueue(teller_queue,gate,currentQueueSize);
    }
}
int main()
{
    FILE* fp=fopen("input1.txt","r");
    FILE* fo=fopen("output.txt","w+");
    TellerQueue teller_queue[10];
    Customer customer;
    int currentQueueSize=0;
    fscanf(fp," %d",&currentQueueSize);
    for(int i=0;i<10;i++)
    {
        teller_queue[i].front=0;
        teller_queue[i].rear=0;
        teller_queue[i].status=0;
        teller_queue[i].queue[0].wait_time=0;
        teller_queue[i].queue[0].ser_time=0;
        teller_queue[i].queue[0].arr_time=0;
        teller_queue[i].count=0;
    }
    for(int i=0;i<currentQueueSize;i++)
    {
        teller_queue[i].status=2;
    }
    char ID[20];
    int arr_time,ser_time;
    while(fscanf(fp,"%s %d %d",ID,&arr_time,&ser_time)!=EOF)
    {
        while(UpdateQueueStatus(teller_queue,arr_time,ID,ser_time,currentQueueSize)==0)
        {
            global_clock++;
            printf("%d\n",global_clock);
        }
        if (ID=="@")
        {
            OpenQueue (teller_queue,ser_time);
            currentQueueSize++;
        }
        else if (ID=="#")
        {
            CloseQueue (teller_queue,ser_time,currentQueueSize);
            currentQueueSize--;
            FromTheSecondElementInCloseQueue(teller_queue,ser_time,currentQueueSize);
        }
        else
        {
            int z=GetTheShortestQueueId(currentQueueSize,teller_queue);
            InsertNewCustomer(z,teller_queue,arr_time,ID,ser_time);
        }
        fprintf(fo,"%s %d %d\n",ID,arr_time,ser_time);
    }
//Process the remaining customers in queues
}

