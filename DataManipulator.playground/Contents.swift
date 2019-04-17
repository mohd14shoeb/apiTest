import Foundation
import PlaygroundSupport
PlaygroundPage.current.needsIndefiniteExecution = true

typealias People = [Person]
struct Person: Codable {
    let id: Int
    let name: String
    let age: Int
    let occupation: String
}

func getData() {
    let session = URLSession.shared
    let urlString = "https://mytestapi-app.herokuapp.com/getall"
    guard let url = URL(string: urlString) else { return }
    var request = URLRequest(url: url)
    request.httpMethod = "GET"
    let task = session.dataTask(with: request) { (data, response, error) in
        if let error = error {
            print(error.localizedDescription)
            return
        }
        guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
                print(response.debugDescription)
                return
        }
        if let data = data {
            if let people = try? JSONDecoder().decode(People.self, from: data) {
                for person in people {
                    print(person.name, person.age, person.occupation, "ID:", person.id)
                }
            }
        }
    }
    task.resume()
}

func newUser(name: String, age: Int, occupation: String) {
    let session = URLSession.shared
    let urlString = "https://mytestapi-app.herokuapp.com/add?name=\(name)&age=\(age)&occupation=\(occupation)"
    guard let url = URL(string: urlString) else { return }
    let request = URLRequest(url: url)
    let task = session.dataTask(with: request)
    task.resume()
}

func deleteUser(withId id: Int) {
    let session = URLSession.shared
    let urlString = "https://mytestapi-app.herokuapp.com/delete/\(id)"
    guard let url = URL(string: urlString) else { return }
    let request = URLRequest(url: url)
    let task = session.dataTask(with: request)
    task.resume()
}

func deleteAll() {
    let session = URLSession.shared
    let urlString = "https://mytestapi-app.herokuapp.com/deleteall"
    guard let url = URL(string: urlString) else { return }
    let request = URLRequest(url: url)
    let task = session.dataTask(with: request)
    task.resume()
}

newUser(name: "TestFromSwift2", age: 1, occupation: "Whatever")
//deleteUser(withId: )
deleteAll()
getData()


