class IfTest{
	public static void main(String[] args){
		int num=2;
		if(num==1)
			sop("monday");
		else if(num==2)
			sop("tueseday");
		else 
			sop("nono");
		
		int x=4;
		if(x==3||x==4||x==5)
			sop(x+"����");
		else if(x==6||x==7||x==8)
			sop(x+"�ļ�");
		else if(x==9||x==10||x==11)
			sop(x+"�＾");
		else if(x==12||x==1||x==2)
			sop(x+"����");
		else 
			sop(x+"�·ݲ�����");
	}
	public static void sop(Object obj){
		System.out.println(obj);
	}
}