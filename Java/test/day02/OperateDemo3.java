class OperateDemo3{
	public static void main(String[] args){
		//sop(Integer.toBinaryString(60));
		int num=60;
		//��ȡ60�����4λ��ͨ��&15;
		int n1=num&15;
		//if(temp1>9)
		sop(n1>9?(char)(n1-10+'A'):n1);
		int temp=num>>>4;
		//��temp��ֵ���������λ�Ļ�ȡ��
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