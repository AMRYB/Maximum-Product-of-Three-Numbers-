# 🟦 **Problem Statement**
You are given an integer array `nums`. Your task is to find three numbers in the array whose product is **maximum** and return that maximum product.

---

## 🌟 **Two Types of Cases for Maximum Product of Three Numbers**

### 🔹 **Case 1: Simple Case with Positive Numbers**
In this scenario, all the numbers in the array are positive, or the problem is straightforward because we just need to pick the **three largest numbers**.

**🟢 Input:**  
`nums = [1,2,3]`  

**🟢 Output:**  
`6`

---

### 🔹 **Case 2: Mixed Numbers (Positive and Negative)**
In this case, the array contains both **positive** and **negative** numbers. Negative numbers can result in a higher product if paired wisely.

#### **✨ Possibilities to Consider:**
1. The product of the **three largest numbers**.
2. The product of the **two smallest (most negative) numbers** and the **largest number**.

**🟢 Input:**  
`nums = [-8, -6, 2, 4, 7]`  

**🟢 Output:**  
`336`

---

### 🔍 **Why do we choose `-8, -6`?**

The reason lies in the multiplication behavior of **negative numbers**. Negative numbers, when multiplied together, can produce a **positive value**, and this value might be much larger than the product of three positive numbers.

- **If we only consider the top three largest numbers:**  
  🔸 The three largest numbers are: `2, 4, 7`.  
  🔸 The product: `2 × 4 × 7 = 56`.

- **If we consider the two smallest numbers (`-8, -6`) and the largest number (`7`):**  
  🔹 The two smallest numbers are: `-8, -6`.  
  🔹 When multiplied together, they give: `-8 × -6 = 48`.  
  🔹 Adding the largest number (`7`) gives:  
     `48 × 7 = 336`.

**💡 Clearly, `336` is much greater than `56`.**
