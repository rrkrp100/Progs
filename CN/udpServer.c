#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<unistd.h>
#include<string.h>
#include<netinet/in.h>
#include<arpa/inet.h>

#define PORT 8080
#define MAXLINE 1024

int main()
{
	int sockfd;
	char buffer[MAXLINE];
	char *hello ="Hello from the sever side";
	struct sockaddr_in servaddr, cliaddr;
	
	// Creating the driver
	
	sockfd=socket(AF_INET, SOCK_DGRAM, 0);
	if(sockfd<0)
	{
		printf("Socket failed\n");
		exit(0);
	}
	
	bzero(&servaddr, sizeof(servaddr));
	bzero(&cliaddr, sizeof(cliaddr));
	
	//filling info
	
	servaddr.sin_family= AF_INET;
	servaddr.sin_addr.s_addr= INADDR_ANY;
	servaddr.sin_port=htons(PORT);
	
	// Binding the socket to the server address
	
	if(bind(sockfd,(const struct sockaddr*)&servaddr,sizeof(servaddr))<0)
	{
		printf("Bind Failed\n");
		exit(0);
	}
	//Recieving the msg
	int n, len;
	n= recvfrom(sockfd, (char*)buffer,MAXLINE,0,( struct sockaddr *)&cliaddr, &len);
	buffer[n]='\0';
	printf("Client: %s\n",buffer);
	
	sendto(sockfd,(const char*)hello,strlen(hello),0,(const struct sockaddr *)&cliaddr,len);
	printf("Msg sent \n");
	
	
	return 0;
	
}

