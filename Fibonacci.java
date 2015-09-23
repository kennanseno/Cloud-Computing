class Fibonacci {
	public static void main(String[] args) {
		//change number array size to get more values
		int[] number = new int[12];
		number[0] = 0;
		number[1] = 1;
		
		for(int count = 2; count < number.length; count++){
			number[count] = number[count-1] + number[count-2];
		}
		for (int count = 1; count < number.length; count++) {
			System.out.println(number[count]);
		}
	}
}