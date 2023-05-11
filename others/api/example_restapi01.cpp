// C++ REST SDK
#include <cpprest/http_listener.h>
#include <cpprest/json.h>

using namespace web;
using namespace http;
using namespace utility;
using namespace http::experimental::listener;

void handle_get(http_request request)
{
    json::value response;
    response["message"] = json::value::string("Hello World!");

    request.reply(status_codes::OK, response);
}

int main()
{
    http_listener listener("http://localhost:8080");
    listener.support(methods::GET, handle_get);

    try
    {
        listener.open().wait();
        std::cout << "Listening on port 8080" << std::endl;

        while (true);
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}