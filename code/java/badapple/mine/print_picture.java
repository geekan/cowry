package badapple_minesweeperver;

import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import javax.imageio.ImageIO;

public class print_picture {
	static int[][][][] iconmap=new int [16][16][16][3];//1为次数，2为列，3为行，4为RGB
	/*
	 * 0	空
	 * 1	1
	 * 2	2
	 * 3	3
	 * 4	4
	 * 5	5
	 * 6	6
	 * 7	7
	 * 8	8
	 * 9	？
	 * 10	雷
	 * 11	错雷
	 * 12	炸雷(红)
	 * 13	？(未翻开)
	 * 14	红旗
	 * 15	空(未翻开)
	 * */
	static int [][]colourmap=new int [16][3];
	static int basewide=80;
	static int basehigh=60;
	
	static int [][][]image_base=new int[basehigh][basewide][3];
	static int [][][]image_extend=new int [basehigh*16][basewide*16][3];

	static String rootpath="Z:/TEM/";
	static String iconroot="Z:/TEM/toproc/icontab.bmp.txt";
	static String iconcolour="Z:/TEM/toproc/icontab.bmp.txt.clp.txt";
	
	public static void main(String[] args) {
		
		
		load_icon();
		
		for(int i=1;i<=400;i++)
		{
			StringBuffer fpsb=new StringBuffer();
			fpsb=fpsb.append(rootpath);
			fpsb=fpsb.append(String.format("%06d", i));
			fpsb=fpsb.append(".bmp.txt");
			String imageloca=fpsb.toString();
			load_text(imageloca);
			tran_2_16x();
			writeimage(imageloca);
		}

	}
	public static void writeimage(String imageloca)
	{
		try {
		BufferedImage image=new BufferedImage(basewide*16, basehigh*16, BufferedImage.TYPE_BYTE_INDEXED);
		for(int i1=0;i1<basehigh*16;i1++)
		{
			for(int i2=0;i2<basewide*16;i2++)
			{
				StringBuffer pixelcolos=new StringBuffer();
				String Rs=Integer.toHexString(image_extend[959-i1][i2][2]);
				if(Rs.length()==1)pixelcolos=pixelcolos.append("0");
				pixelcolos=pixelcolos.append(Rs);
				
				String Gs=Integer.toHexString(image_extend[959-i1][i2][1]);
				if(Gs.length()==1)pixelcolos=pixelcolos.append("0");
				pixelcolos=pixelcolos.append(Gs);
				
				String Bs=Integer.toHexString(image_extend[959-i1][i2][0]);
				if(Bs.length()==1)pixelcolos=pixelcolos.append("0");
				pixelcolos=pixelcolos.append(Bs);
				//System.out.print(pixelcolos+"\t");
				//System.out.println(Integer.parseInt(pixelcolos.toString(), 16));
				image.setRGB(i2, i1,Integer.parseInt(pixelcolos.toString(), 16));
				//image.setRGB(i2, i1,0xFF0000);
			}
		}
		ImageIO.write(image, "PNG", new File(imageloca+"(g).png"));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void tran_2_16x()
	{
		//主框架
		for(int i1=0;i1<basehigh*16;i1+=16)
		{
			for(int i2=0;i2<basewide*16;i2+=16)
			{
				int icon=image_base[i1/16][i2/16][0];
				//填充雷
				for(int i3=0;i3<16;i3++)
				{
					for(int i4=0;i4<16;i4++)
					{
						//上色
						for(int i5=0;i5<3;i5++)
						{
							image_extend[i1+i3][i2+i4][i5]=iconmap[icon][i3][i4][i5];
						}
					}
				}
			}
		}
		/*
		for(int i1=0;i1<960;i1++)
		{
			for(int i2=0;i2<1280;i2++)
			{
				for(int i3=0;i3<3;i3++)
				{
					System.out.printf("%4d",image_extend[i1][i2][i3]);
				}
				System.out.print("|");
			}
			System.out.println();
		}
		*/
	}
	
	public static int imageredefine(int inside)
	{
		switch (inside) {
		case 1:
			return 1;
		case 2:
			return 2;
		case 3:
			return 3;
		case 4:
			return 4;
		case 5:
			return 5;
		case 6:
			return 6;
		case 7:
			return 7;
		case 8:
			return 8;
			/*
			 * 0	空
			 * 1	1
			 * 2	2
			 * 3	3
			 * 4	4
			 * 5	5
			 * 6	6
			 * 7	7
			 * 8	8
			 * 9	？
			 * 10	雷
			 * 11	错雷
			 * 12	炸雷(红)
			 * 13	？(未翻开)
			 * 14	红旗
			 * 15	空(未翻开)
			 * */
			//-1为白,-2灰,-3黑
		case -1:
			return 0;
		case -2:
			return 9;
		case -3:
			return 12;
		default:
			return 0;
		}
	}
	public static void load_text(String imageloca)
	{
		try {
			File pioc=new File(imageloca);
			System.out.println(pioc.canRead());
			BufferedReader readtext=new BufferedReader(new FileReader(new File(imageloca)));
			for(int i1=0;i1<basehigh;i1++)
			{
				String inline=readtext.readLine();
				String []spinline=inline.split("\t");
				for(int i2=0;i2<basewide;i2++)
				{
					image_base[i1][i2][0]=imageredefine(Integer.parseInt(spinline[i2]));
				}
			}
			readtext.close();
			/*
			for(int i1=0;i1<60;i1++)
			{
				for(int i2=0;i2<80;i2++)
				{
					System.out.printf("%4d",image_base[i1][i2][0]);
				}
				System.out.println();
			}*/
			
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void load_icon()
	{
		try {
			BufferedReader readicon=new BufferedReader(new FileReader(new File(iconroot)));
			for(int i1=0;i1<16;i1++)
			{
				for(int i2=0;i2<16;i2++)
				{
					String inline=readicon.readLine();
					String []spinline=inline.split("\t");
					for(int i3=0;i3<16;i3++)
					{
						iconmap[i1][i2][i3][0]=Integer.parseInt(spinline[i3]);
					}
				}
			}
			/*
			for(int i1=0;i1<16;i1++)
			{
				for(int i2=0;i2<16;i2++)
				{
					for(int i3=0;i3<16;i3++)
					{
						System.out.printf("%2d ",iconmap[i1][i2][i3][0]);
					}
					System.out.println();
				}
				System.out.println();
			}
			*/
			readicon.close();
			
			BufferedReader readcolour=new BufferedReader(new FileReader(new File(iconcolour)));
			for(int i1=0;i1<16;i1++)
			{
				String colodef[]=readcolour.readLine().split("\t");
				for(int i2=1;i2<=3;i2++)
				{
					colourmap[i1][i2-1]=Integer.parseInt(colodef[i2]);
				}
			}
			/*
			for(int i1=0;i1<16;i1++)
			{
				for(int i2=0;i2<3;i2++)
				{
					System.out.printf("%5d",colourmap[i1][i2]);
				}
				System.out.println();
			}
			*/
			readcolour.close();

			for(int i1=0;i1<16;i1++)
			{
				for(int i2=0;i2<16;i2++)
				{
					for(int i3=0;i3<16;i3++)
					{
						int coloid=iconmap[i1][i2][i3][0];
						for(int i4=0;i4<3;i4++)
						{
							iconmap[i1][i2][i3][i4]=colourmap[coloid][i4];
						}
					}
				}
			}
			/*
			for(int i1=0;i1<16;i1++)
			{
				for(int i2=0;i2<16;i2++)
				{
					for(int i3=0;i3<16;i3++)
					{
						for(int i4=0;i4<3;i4++)
						{
							System.out.printf("%5d ",iconmap[i1][i2][i3][i4]);
						}
						System.out.print("||");
					}
					System.out.println();
				}
				System.out.println();
			}
			*/
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
