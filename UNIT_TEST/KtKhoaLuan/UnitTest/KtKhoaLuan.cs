using KtKhoaLuan;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;

namespace UnitTest
{
    [TestClass]
    public class KtKhoaLuan
    {

        [TestMethod]
        //n<5: n=2; []diem = {10,7}; diemDoAn = 9 -> False
        public void Test1()
        {
            int n = 2;
            double diemDoAn = 9;
            double[] diem = new double[] { 10,7};
            bool expected = false;
            KhoaLuan khoaLuan = new KhoaLuan();
            Assert.AreEqual(expected, khoaLuan.KtKhoaLuan(diem,n,diemDoAn));

        }

        [TestMethod]
        //n>=5, dem>2: n=6; []diem = {3,4,8,7,9,4}; diemDoAn = 8 -> dem=3 -> False
        public void Test2()
        {
            int n = 6;
            double diemDoAn = 8;
            double[] diem = new double[] { 3, 4, 8, 7, 9, 4 };
            bool expected = false;
            KhoaLuan khoaLuan = new KhoaLuan();
            Assert.AreEqual(expected, khoaLuan.KtKhoaLuan(diem, n, diemDoAn));
        }

        [TestMethod]
        //n>=5, dem<=2, !(tb >= 7.0 && diemDoAn >= 8): n=5; []diem = {6,6,7,7,8}; diemDoAn = 8 -> tb=6,8; dem=0 -> False
        public void Test3()
        {
            int n = 5;
            double diemDoAn = 8;
            double[] diem = new double[] { 6, 6, 7, 7, 8 };
            bool expected = false;
            KhoaLuan khoaLuan = new KhoaLuan();
            Assert.AreEqual(expected, khoaLuan.KtKhoaLuan(diem, n, diemDoAn));
        }

        [TestMethod]
        //n>=5, dem<=2, (tb >= 7.0 && diemDoAn >= 8): n=5; []diem = {4,7,8,9,9}; diemDoAn = 9 -> tb=7.4; dem=1 -> False
        public void Test4()
        {
            int n = 5;
            double diemDoAn = 9;
            double[] diem = new double[] { 4, 7, 8, 9, 9 };
            bool expected = true;
            KhoaLuan khoaLuan = new KhoaLuan();
            Assert.AreEqual(expected, khoaLuan.KtKhoaLuan(diem, n, diemDoAn));
        }

    }
}
