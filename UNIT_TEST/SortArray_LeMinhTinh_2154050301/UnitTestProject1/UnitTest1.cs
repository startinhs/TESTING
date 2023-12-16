using LeMinhTinh_2154050301;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;

namespace UnitTestProject1
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        //Truong hop break 
        public void TestSortOptimizedArray1()
        {
            int n = 4;
            int []mang = new int[] { 1, 2, 3, 4 };
            SortArray s = new SortArray();
            int[] expected = new int[] { 1, 2, 3, 4 };
            int[] actual = s.SortOptimizedArray(mang, n);
            for (int i = 0; i < n; i++)
            {
                Assert.AreEqual(expected[i], actual[i]);
            }
            //CollectionAssert.AreEqual(expected, actual);
        }

        [TestMethod]
        //Truong hop break
        public void TestSortOptimizedArray2()
        {
            int n = 5;
            int[] mang = new int[] { 5, 4, 3, 1, 2 };
            SortArray s = new SortArray();
            int[] expected = new int[] { 1, 2, 3, 4, 5 };
            int[] actual = s.SortOptimizedArray(mang, n);
            for (int i = 0; i < n; i++)
            {
                Assert.AreEqual(expected[i], actual[i]);
            }
            //CollectionAssert.AreEqual(expected, actual);
        }

        [TestMethod]
        //Truong hop return
        public void TestSortOptimizedArray3()
        {
            int n = 5;
            int[] mang = new int[] { 5, 4, 3, 2, 1 };
            SortArray s = new SortArray();
            int[] expected = new int[] {1, 2, 3, 4, 5 };
            int[] actual = s.SortOptimizedArray(mang, n);
            for (int i = 0; i < n; i++)
            {
                Assert.AreEqual(expected[i], actual[i]);
            }
            //CollectionAssert.AreEqual(expected, actual);
        }
    }
}
