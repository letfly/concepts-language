class OperateDemo1{
	public static void main(String[] args){
		int x=3;
		x=x+4;
		short s=4;
		// s=s+2;
        s+=2; // 会做一个自动转换动作
		
		int a,b,c;
		a=b=c=5;
		sop(s<4);
	}
	public static void sop(Object obj){
		System.out.println(obj);
	}
}
