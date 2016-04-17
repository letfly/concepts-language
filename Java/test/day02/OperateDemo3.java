class OperateDemo3{
	public static void main(String[] args){
		//sop(Integer.toBinaryString(60));
		int num=60;
		//获取60的最低4位，通过&15;
		int n1=num&15;
		//if(temp1>9)
		sop(n1>9?(char)(n1-10+'A'):n1);
		int temp=num>>>4;
		//对temp的值进行最低四位的获取。
		int n2=temp&15;
		//if(n2>9)
		sop(n2>9?(char)('A'+n2-10):n2);
		
		int x=1,y;
		y=x>1?100:200;
		sop("y="+y);
	}
	public static void sop(Object obj){
		System.out.println(obj);
	}
}