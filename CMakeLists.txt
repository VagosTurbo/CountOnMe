cmake_minimum_required(VERSION 3.0)
project(CountOnMe)

set(CPACK_PACKAGE_NAME ${PROJECT_NAME}) 
set(CPACK_PACKAGE_VENDOR "CountOnMe Team")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "CountOnMe is a simple calculator")
set(CPACK_PACKAGE_VERSION "1.0.0")


set(CPACK_GENERATOR DEB)
install(DIRECTORY deployment_linux/ DESTINATION opt/${PROJECT_NAME})
install(FILES deployment_linux/${PROJECT_NAME}.desktop DESTINATION share/applications)
set(CPACK_DEBIAN_PACKAGE_CONTROL_EXTRA "${CMAKE_CURRENT_SOURCE_DIR}/linux/postinst;")

include(CPack)