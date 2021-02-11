func maxProfit(prices []int) int {
    
    var min = prices[0]
    var profit = 0
    for i:=0; i<len(prices); i++{
        
        // 오르면 일단 판다
        if min < prices[i]{
            var temp = prices[i] - min
            if temp > profit{
                profit = temp // 팔았을때 최대 이익이 변동이 없으면 내둔다
            }
        }
        
        // 더 낮은 가격으로 살수있으면 산다
        if prices[i] < min {
            min = prices[i]
        }
        
    }
    return profit
}
