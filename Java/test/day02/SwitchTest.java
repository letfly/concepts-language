class SwitchTest{
	public static void main(String[] args){
		int x=4;
		switch(x){
			case 3:
			case 4:
			case 5:
				sop(x+"´º¼¾");
				break;
			case 6:
			case 7:
			case 8:
				sop(x+"ÏÄ¼¾");
				break;
			case 9:
			case 10:
			case 11:
				sop(x+"Çï¼¾");
				break;
			case 12:
			case 1:
			case 2:
				sop(x+"¶¬¼¾");
				break;
			default:
				sop("²»´æÔÚ");
		}
	}
	public static void sop(Object obj){
		System.out.println(obj);
	}
}