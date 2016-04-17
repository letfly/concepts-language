class SwitchDemo{
	public static  void main(String[] args){
		int x=3;
		switch(x){
			default:
				sop("d");
			case 4:
				sop("a");
			case 6:
				sop("b");
				break;
			case 2:
				sop("c");				
		}
	}
	public static void sop(Object obj){
		System.out.println(obj);
	}
}