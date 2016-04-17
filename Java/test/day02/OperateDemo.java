class OperateDemo{
	public static void main(String[ ]args){
		sop("hello\rworld ");
		sop("\\hello\\");
		char ch='\'';
		char c='a';
		sop(ch);
	}
	public static void sop(Object obj){
		System.out.println(obj);
	}
}
