using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeMinhTinh_2154050301
{
    public class SortArray
    {
        public int[] SortOptimizedArray(int[] mang, int n)
        {
            bool swapRequired;
            for (int i = 0; i < n - 1; i++)
            {
                swapRequired = false;
                for (int j = 0; j < n - i - 1; j++)
                    if (mang[j] > mang[j + 1])
                    {
                        var tempVar = mang[j];
                        mang[j] = mang[j + 1];
                        mang[j + 1] = tempVar;
                        swapRequired = true;
                    }
                if (swapRequired == false)
                    break;
            }
            return mang;
        }
    }
}
