class SwitchTest{
	public static void main(String[] args){
		int x=4;
		switch(x){
			case 3:
			case 4:
			case 5:
				sop(x+"����");
				break;
			case 6:
			case 7:
			case 8:
				sop(x+"�ļ�");
				break;
			case 9:
			case 10:
			case 11:
				sop(x+"�＾");
				break;
			case 12:
			case 1:
			case 2:
				sop(x+"����");
				break;
			default:
				sop("������");
		}
	}
	public static void sop(Object obj){
		System.out.println(obj);
	}
}