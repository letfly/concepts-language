class OperateDemo2{
	public static void main(String[] args){
		//int x=4;
		//�߼��������������boolean���͵ı��ʽ
		//��򣺵�ͬΪ�٣���Ϊ��
		//sop(x>3&&x<7);
		/*
		&��&&���ص㣺
		&�����������true��false���ұ߶�����
		&&���������falseʱ���ұ߲�����
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