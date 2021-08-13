//
//  SWExtensions.swift
//  ShinePhone
//
//  Created by Hut on 2021/5/26.
//  Copyright © 2021 Growatt New Energy Technology CO.,LTD. All rights reserved.
//

import Foundation

// MARK: - 时间格式本地化
extension TimeZone {
    static let gmt = TimeZone(secondsFromGMT: 0)!
}
extension Formatter {
    static let date = DateFormatter()
}

extension Date {
    func localizedDescription(dateStyle: DateFormatter.Style = .medium,
                              timeStyle: DateFormatter.Style = .medium,
                           in timeZone : TimeZone = .current,
                              locale   : Locale = .current) -> String {
        Formatter.date.locale = locale
        Formatter.date.timeZone = timeZone
        Formatter.date.dateStyle = dateStyle
        Formatter.date.timeStyle = timeStyle
        return Formatter.date.string(from: self)
    }
    var localizedDescription: String { localizedDescription() }
    
    /// 一天的开始时间 2021-04-18 16:00:00 +0000
    var startOfDay: Date {
        return Calendar.current.startOfDay(for: self)
    }

    /// 一个月的开始时间  2021-03-31 16:00:00 +0000
    var startOfMonth: Date {
        let calendar = Calendar(identifier: .gregorian)
        let components = calendar.dateComponents([.year, .month], from: self)
        return  calendar.date(from: components)!
    }

    /// 一天的结束时间 2021-04-19 15:59:59 +0000
    var endOfDay: Date {
        var components = DateComponents()
        components.day = 1
        components.second = -1
        return Calendar.current.date(byAdding: components, to: startOfDay)!
    }

    /// 一月的结束时间 2021-04-30 15:59:59 +0000
    var endOfMonth: Date {
        var components = DateComponents()
        components.month = 1
        components.second = -1
        return Calendar(identifier: .gregorian).date(byAdding: components, to: startOfMonth)!
    }

    /// 是否为星期一
    func isMonday() -> Bool {
        let calendar = Calendar(identifier: .gregorian)
        let components = calendar.dateComponents([.weekday], from: self)
        return components.weekday == 2
    }
}


extension Dictionary {
    func getIntValue(fromKey key:String) -> Int? {
        var value: Int?
        guard let info = self as? [String: Any] else {
            return nil
        }
        if let num = info[key] as? Int {
            value = num
        } else if let str = info[key] as? String {
            value = Int(str)
        } else {
            value = nil
        }
        return value
    }
    
    func getUIntValue(fromKey key:String) -> UInt? {
        var value: UInt?
        guard let info = self as? [String: Any] else {
            return nil
        }
        if let num = info[key] as? UInt {
            value = num
        } else if let str = info[key] as? String {
            value = UInt(str)
        } else {
            value = nil
        }
        return value
    }
    
    func getDoubleValue(fromKey key:String) -> Double? {
        var value: Double?
        guard let info = self as? [String: Any] else {
            return nil
        }
        if let num = info[key] as? Double {
            value = num
        } else if let str = info[key] as? String {
            value = Double(str)
        } else {
            value = nil
        }
        return value
    }
    
    func getFloatValue(fromKey key:String) -> Float? {
        var value: Float?
        guard let info = self as? [String: Any] else {
            return nil
        }
        if let num = info[key] as? Float {
            value = num
        } else if let str = info[key] as? String {
            value = Float(str)
        } else {
            value = nil
        }
        return value
    }
    
    func getBoolValue(fromKey key:String) -> Bool? {
        var value: Bool?
        guard let info = self as? [String: Any] else {
            return nil
        }
        if let num = info[key] as? Bool {
            value = num
        } else if let str = info[key] as? String {
            value = Bool(str)
        } else {
            value = nil
        }
        return value
    }
}


extension String {
    /// 使用正则表达式进行匹配
    func matches(for regex: String) -> [String] {
        do {
            let text = self as String
            let regex = try NSRegularExpression(pattern: regex)
            let result = regex.matches(in: text,
                                       range: NSRange(text.startIndex..., in: text))
            
            return result.map {String(text[Range($0.range, in: text)!]) }
        } catch let error {
            print("invalid regex: \(error.localizedDescription)")
            return []
        }
    }
    
    /// 使用正则表达式进行匹配(可分组)
    func matcheGroups(for regexPattern: String) -> [[String]] {
        do {
            let text = self
            let regex = try NSRegularExpression(pattern: regexPattern)
            let matches = regex.matches(in: text,
                                        range: NSRange(text.startIndex..., in: text))
            return matches.map { match in
                return (0..<match.numberOfRanges).map {
                    let rangeBounds = match.range(at: $0)
                    guard let range = Range(rangeBounds, in: text) else {
                        return ""
                    }
                    return String(text[range])
                }
            }
        } catch let error {
            print("invalid regex: \(error.localizedDescription)")
            return []
        }
    }

}
