#include <unoio.h>
#include <stdlib.h>
#include <stdio.h>
#include<gavthiserial.h>
#define F_CPU 16000000ul
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

const int ROWS = 4; //four rows
const int COLS = 3; //three columns
int keys[ROWS][COLS] = {
  {1,2,3},
  {4,5,6},
  {7,8,9},
  {0,0,0}
};

byte rowpins[ROWS] = {A0, A1, A2, A3};
byte colpins[COLS] = {A4, A5, 13};

void Send2Pachube(int a)
{
  char b[10];

itoa(a,b,10);
  
   serialprintln("AT");
  _delay_ms(1000);

  serialprintln("AT+CPIN?");
  _delay_ms(1000);

  serialprintln("AT+CREG?");
  _delay_ms(1000);

  serialprintln("AT+CGATT?");
  _delay_ms(1000);

  serialprintln("AT+CIPSHUT");
  _delay_ms(1000);

  serialprintln("AT+CIPSTATUS");
  _delay_ms(1000);

  serialprintln("AT+CIPMUX=0");
  _delay_ms(1000);
 
  serialprintln("AT+CSTT=\"bsnlnet\"");//start task and setting the APN,
  _delay_ms(1000);
 
  serialprintln("AT+CIICR");//bring up wireless connection
  _delay_ms(2000);
 
  serialprintln("AT+CIFSR");//get local IP adress
  _delay_ms(2000);
 
  serialprintln("AT+CIPSPRT=0");
  _delay_ms(2000);
 
  serialprintln("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"");//start up the connection
  _delay_ms(2000);
 
  serialprintln("AT+CIPSEND");//begin send data to remote server
  _delay_ms(2000);
  
    char str[]="GET http://api.thingspeak.com/update?api_key=JCYMISBP2JXYERVT&field1=0";
    strcat(str, b);
  serialprintln(str);//begin send data to remote server
  _delay_ms(2000);
  

  serialprintln((char)26);//sending
  _delay_ms(2000);//waitting for reply, important! the time is base on the condition of internet 

  
 
  serialprintln("AT+CIPSHUT");//close the connection
  _delay_ms(100);
}

void Send3Pachube(int a)
{
  char b[10];

itoa(a,b,10);
  
   serialprintln("AT");
  _delay_ms(1000);

  serialprintln("AT+CPIN?");
  _delay_ms(1000);

  serialprintln("AT+CREG?");
  _delay_ms(1000);

  serialprintln("AT+CGATT?");
  _delay_ms(1000);

  serialprintln("AT+CIPSHUT");
  _delay_ms(1000);

  serialprintln("AT+CIPSTATUS");
  _delay_ms(1000);

  serialprintln("AT+CIPMUX=0");
  _delay_ms(1000);
 
  serialprintln("AT+CSTT=\"bsnlnet\"");//start task and setting the APN,
  _delay_ms(1000);
 
  serialprintln("AT+CIICR");//bring up wireless connection
  _delay_ms(2000);
 
  serialprintln("AT+CIFSR");//get local IP adress
  _delay_ms(2000);
 
  serialprintln("AT+CIPSPRT=0");
  _delay_ms(2000);
 
  serialprintln("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"");//start up the connection
  _delay_ms(2000);
 
  serialprintln("AT+CIPSEND");//begin send data to remote server
  _delay_ms(2000);
  
    char str[]="GET http://api.thingspeak.com/update?api_key=JCYMISBP2JXYERVT&field2=0";
    strcat(str, b);
  serialprintln(str);//begin send data to remote server
  _delay_ms(2000);
  

  serialprintln((char)26);//sending
  _delay_ms(2000);//waitting for reply, important! the time is base on the condition of internet 

  
 
  serialprintln("AT+CIPSHUT");//close the connection
  _delay_ms(100);
}

void Send4Pachube(char a[])
{
  
   serialprintln("AT");
  _delay_ms(1000);

  serialprintln("AT+CPIN?");
  _delay_ms(1000);

  serialprintln("AT+CREG?");
  _delay_ms(1000);

  serialprintln("AT+CGATT?");
  _delay_ms(1000);

  serialprintln("AT+CIPSHUT");
  _delay_ms(1000);

  serialprintln("AT+CIPSTATUS");
  _delay_ms(1000);

  serialprintln("AT+CIPMUX=0");
  _delay_ms(1000);
 
  serialprintln("AT+CSTT=\"bsnlnet\"");//start task and setting the APN,
  _delay_ms(1000);
 
  serialprintln("AT+CIICR");//bring up wireless connection
  _delay_ms(2000);
 
  serialprintln("AT+CIFSR");//get local IP adress
  _delay_ms(2000);
 
  serialprintln("AT+CIPSPRT=0");
  _delay_ms(2000);
 
  serialprintln("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"");//start up the connection
  _delay_ms(2000);
 
  serialprintln("AT+CIPSEND");//begin send data to remote server
  _delay_ms(2000);
  
    char str[]="GET http://api.thingspeak.com/update?api_key=JCYMISBP2JXYERVT&field3=0";
    strcat(str, a);
  serialprintln(str);//begin send data to remote server
  _delay_ms(2000);
  

  serialprintln((char)26);//sending
  _delay_ms(2000);//waitting for reply, important! the time is base on the condition of internet 

  
 
  serialprintln("AT+CIPSHUT");//close the connection
  _delay_ms(100);
}

void Send5Pachube(char a[])
{
  char b[10];

itoa(a,b,10);
  
   serialprintln("AT");
  _delay_ms(1000);

  serialprintln("AT+CPIN?");
  _delay_ms(1000);

  serialprintln("AT+CREG?");
  _delay_ms(1000);

  serialprintln("AT+CGATT?");
  _delay_ms(1000);

  serialprintln("AT+CIPSHUT");
  _delay_ms(1000);

  serialprintln("AT+CIPSTATUS");
  _delay_ms(1000);

  serialprintln("AT+CIPMUX=0");
  _delay_ms(1000);
 
  serialprintln("AT+CSTT=\"bsnlnet\"");//start task and setting the APN,
  _delay_ms(1000);
 
  serialprintln("AT+CIICR");//bring up wireless connection
  _delay_ms(2000);
 
  serialprintln("AT+CIFSR");//get local IP adress
  _delay_ms(2000);
 
  serialprintln("AT+CIPSPRT=0");
  _delay_ms(2000);
 
  serialprintln("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"");//start up the connection
  _delay_ms(2000);
 
  serialprintln("AT+CIPSEND");//begin send data to remote server
  _delay_ms(2000);
  
    char str[]="GET http://api.thingspeak.com/update?api_key=JCYMISBP2JXYERVT&field4=0";
    strcat(str, a);
  serialprintln(str);//begin send data to remote server
  _delay_ms(2000);
  

  serialprintln((char)26);//sending
  _delay_ms(2000);//waitting for reply, important! the time is base on the condition of internet 

  
 
  serialprintln("AT+CIPSHUT");//close the connection
  _delay_ms(100);
}
int getkey()
{
      digitalwrite(colpins[0],1);
      digitalwrite(colpins[1],1);
      digitalwrite(colpins[2],1);
  for(int i=0;i<COLS;i++)
  {
    digitalwrite(colpins[i],0);
    for(int j=0;j<ROWS;j++){
    if(!digitalread(rowpins[j])){
      while(!digitalread(rowpins[j]));
      digitalwrite(colpins[i],1);
      return(keys[j][i]);
    }
    }
    digitalwrite(colpins[i],1);
    
  }
  _delay_ms(200);
  return(10);
}
/*
String ConvertLat()
{
  String posneg = "";
  if (nmea[3] == "S") {
    posneg = "-";
  }
  String latfirst;
  float latsecond;
  for (int i = 0; i < nmea[2].length(); i++) {
    if (nmea[2].substring(i, i + 1) == ".") {
      latfirst = nmea[2].substring(0, i - 2);
      latsecond = nmea[2].substring(i - 2).toFloat();
    }
  }
  latsecond = latsecond / 60;
  String CalcLat = "";

  char charVal[9];
  dtostrf(latsecond, 4, 6, charVal);
  for (int i = 0; i < sizeof(charVal); i++)
  {
    CalcLat += charVal[i];
  }
  latfirst += CalcLat.substring(1);
  latfirst = posneg += latfirst;
  return latfirst;
}

String ConvertLng() 
{
  String posneg = "";
  if (nmea[5] == "W") {
    posneg = "-";
  }

  String lngfirst;
  float lngsecond;
  for (int i = 0; i < nmea[4].length(); i++) {
    if (nmea[4].substring(i, i + 1) == ".") {
      lngfirst = nmea[4].substring(0, i - 2);
      //Serial.println(lngfirst);
      lngsecond = nmea[4].substring(i - 2).toFloat();
      //Serial.println(lngsecond);

    }
  }
  lngsecond = lngsecond / 60;
  String CalcLng = "";
  char charVal[9];
  dtostrf(lngsecond, 4, 6, charVal);
  for (int i = 0; i < sizeof(charVal); i++)
  {
    CalcLng += charVal[i];
  }
  lngfirst += CalcLng.substring(1);
  lngfirst = posneg += lngfirst;
  return lngfirst;

  
}*/

int Rand(int lower, int upper, int count=1) 
{ 
    int i; 
    for (i = 0; i < count; i++) { 
        int num = (rand() % 
           (upper - lower + 1)) + lower; 
        return(num);
    } 
} 

void ftoa(float n, char* res, int afterpoint) 
{ 
    // Extract integer part 
    int ipart = (int)n; 
  
    // Extract floating part 
    float fpart = n - (float)ipart; 
  
    // convert integer part to string 
    int i = itoa(ipart, res, 0); 
  
    // check for display option after point 
    if (afterpoint != 0) { 
        res[i] = '.'; // add dot 
  
        // Get the value of fraction part upto given no. 
        // of points after dot. The third parameter  
        // is needed to handle cases like 233.007 
        fpart = fpart * pow(10, afterpoint); 
  
        itoa((int)fpart, res + i + 1, afterpoint); 
    } 
} 



enum
{
CMD=0,
DATA,
};
 
char buf[100];
volatile char ind,flag,stringReceived;
char gpgga[]={'$','G','P','G','G','A'};
float longitu;
float latitu;
char latitude[12];
char logitude[12];
char lat[12];
char longi[12];
int whole1,whole2,entered_1[4],entered_2[4],num1=0,num2=0,flag1=0,flag2=0,k=0;
int random1=0,random2=0,q1,q2;
char OTP1[4],OTP2[4],temp,tem;
int b=0,d=0,u=0,r=0;
float c[2],e;


int main()
{
 pinmode(12,2);   //access
 pinmode(A0,2);   //keypad i/p
 pinmode(A1,2);
 pinmode(A2,2);
 pinmode(A3,2);
 pinmode(A4,1);   //keypad o/p
 pinmode(A5,1);
 pinmode(13,1);
 pinmode(11,1);

 pinmode(9,0);    //ultra 1
pinmode(2,1);
pinmode(8,0);     //ultra 2
pinmode(3,1);

PCICR |= (1<<PCIE0);    //pin change interrupt
PCMSK0 |= (1<<1);
PCICR |= (1<<PCIE0);
PCMSK0 |= (1<<0);

sei();

TCCR0B|=(1<<CS02);    
TCCR0B&=~(1<<CS01);    //prescaler 256 
TCCR0B|=(1<<CS00);     

digitalwrite(2,0);
digitalwrite(3,0);

 serialbegin(9600);
 
while(1)
{

digitalwrite(2,0);
_delay_us(10);
digitalwrite(2,1);
_delay_us(10);
digitalwrite(2,0);
_delay_ms(500);
d^=1;

digitalwrite(3,0);
_delay_us(10);
digitalwrite(3,1);
_delay_us(10);
digitalwrite(3,0);
_delay_ms(500);
//Serial.print("hi");
e=(c[0]+c[1])/2;
//serialprintln(e);
d^=1;


 if(stringReceived == 1)
{
cli();
serialprint("Received String:");
for(int i=0;i<ind;i++)
serialprint(buf[i]);
ind=0;
stringReceived=0;
//serialprintln(" ");
//serialprint("Latitude:");
for(int i=18,r=0;i<27;i++)
{
latitude[i]=buf[i];
lat[r]=latitude[i];
//serialprint(latitude[i]);
r++;
}
//serialprintln(" ");
//serialprint("Logitude:");
for(int i=31, u=0;i<40;i++)
{
logitude[i]=buf[i];
longi[u]=logitude[i];

//serialprint(longi[i]);
 u++;
}
serialprintln(" ");
_delay_ms(2000);
sei();

tem=longi[4];
longi[4]=longi[3];
longi[3]=longi[2];
longi[2]=tem;

tem=lat[4];
lat[4]=lat[3];
lat[3]=lat[2];
lat[2]=tem;

//longitu=atof(longi);
//longitu=longitu/100;
//ftoa(longitu,longi,12);
//latitu=atof(lat);
//latitu=latitu/100;
//ftoa(latitu,lat,12);

serialprint("Logitude:");
for(int i=0;i<9;i++)
{
serialprint(longi[i]);
}
serialprintln(" ");
serialprint("Latitude:");
for(int i=0;i<9;i++)
{
serialprint(lat[i]);
}
serialprintln(" ");
//serialprint(longitu);
//serialprint(latitu);
}



  
  if(!digitalread(12))
  {
    flag1=0,flag2=0;
    q1=random(1000,10000);
//    random1=q1;
    q2=random(1000,10000);
//    random2=q2;
    _delay_ms(2);
//    Send2Pachube(q1);
//    _delay_ms(500);
//    Send3Pachube(q2);
    serialprint(q1);
    serialprint(q2);

    
    for(int j=0;k<1;j++)
    {
      int temp=getkey();
      if(temp!=10)
      {
        
//      serialprintln(temp);
        if(num1<4){
        entered_1[num1]=temp;
        num1++;
        serialprintln(temp);
        }
        else{
        entered_2[num2]=temp;
        num1++;
        num2++;
        serialprintln(temp);
        }
      }

      if(num1==8)
      break;
    }
          whole1=entered_1[0]*1000+entered_1[1]*100+entered_1[2]*10+entered_1[3];
            whole2=entered_2[0]*1000+entered_2[1]*100+entered_2[2]*10+entered_2[3];
//    while(num2!=4)
//    {
//      char temp=getkey();
//      if(temp!='w')
//      {
//        entered_2[num2]=temp;
//        num2++;
//        serialprintln(temp);
//      }
//    }
num1=0,num2=0;
    

      if(whole1==q1)
      {
        flag1++;
      }

      if(whole2==q2)
      {
        flag2++;
      }
            serialprintln(q1);
        serialprintln("flag1");
    serialprintln("flag2");
    serialprintln(q1);
    serialprintln(q2);
    if(flag1 && flag2)
    {
      serialprintln("Done");
      digitalwrite(11,1);
    }
    
  }
  
  
  else if(e>50)
  {

UCSR0B &= ~(1<<RXEN0);
    _delay_ms(1000);
        serialprintln("AT+CMGF=1");//+\r\n");
    _delay_ms(1000);

    serialprintln("AT+CMGS=\"9405958834\"\r");//+\r\n");
    _delay_ms(1000);//    Serial.print("5");

    serialprintln("FuelLow");//+\r\n");
    _delay_ms(1000);//    Serial.print("6");

    serialprintln(char(26));//\r\n");
    _delay_ms(1000);

//      serialprintln("AT+CIPSHUT");//close the connection
//  _delay_ms(100);

  UCSR0B |= (1<<RXEN0);
//    confirm++;
    }
    
//UCSR0B &= ~(1<<RXEN0);
//    Send4Pachube(lat);  
//    Send5Pachube(longi);
//      UCSR0B |= (1<<RXEN0);
  }





  
 






}

ISR(PCINT0_vect)
{
if(!b)
{TCNT0=0; b=1;}
else
{c[d]=TCNT0;c[d]=1.1*c[d];b=0;  
//Serial.println(c);
}
}


ISR(USART_RX_vect)
{
char ch=UDR0;
buf[ind]=ch;
ind++;
if(ind<7)
{
if(buf[ind-1] != gpgga[ind-1])               // $GPGGA
ind=0;
}
if(ind>=50)
stringReceived=1;
}
