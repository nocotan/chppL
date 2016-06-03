#include <boost/python.hpp>
#include <string>

#define self (*this)

class ChpplData {
  private:
    std::string url;
    std::string description;
  public:
    std::string get_url();
    void set_url(std::string url);
    std::string get_description();
    void set_description(std::string description);
};


std::string ChpplData::get_url() {
  return self.url;
}

void ChpplData::set_url(std::string url) {
  self.url = url;
}

std::string ChpplData::get_description() {
  return self.description;
}

void ChpplData::set_description(std::string description) {
  self.description = description;
}


BOOST_PYTHON_MODULE(chppl_data) {
  namespace python = boost::python;

  python::class_<ChpplData>("ChpplData", python::init<>())
    .def("get_url", &ChpplData::get_url)
    .def("set_url", &ChpplData::set_url)
    .def("get_description", &ChpplData::get_description)
    .def("set_description", &ChpplData::set_description);
}
