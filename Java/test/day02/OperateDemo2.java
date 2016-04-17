class OperateDemo2{
	public static void main(String[] args){
		//int x=4;
		//逻辑运算符用于连接boolean类型的表达式
		//异或：当同为假，异为真
		//sop(x>3&&x<7);
		/*
		&和&&的特点：
		&：无论左边是true是false，右边都运算
		&&：当左边是false时，右边才运算
		*/
		sop(~6);
		
		int x=4,y=6;
		x=x^y;
		y=x^y;
		x=x^y;
		sop(x);
		sop(y);
	}
	public static void sop(Object obj){
		System.out.println(obj);
	}
}