using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KtKhoaLuan
{
    public class KhoaLuan
    {
        public KhoaLuan() { }
        public bool KtKhoaLuan(double []diem, int n, double diemDoAn)
        {
            if(n<5)
                return false;

            int dem = 0;
            double tb = 0;
            for(int i = 0; i < n; i++)
            {
                tb += diem[i];
                if (diem[i] < 5)
                    dem++;
                if(dem>2)
                    return false;
            }
            tb = tb / n;
            if (tb >= 7.0 && diemDoAn >= 8)
                return true;
            return false;
        }
    }
}
